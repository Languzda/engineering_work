import { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import PropTypes from "prop-types";

import Container from "./Container.jsx";
import Button from "./Utils/Button.jsx";

import "./Monit.css";
import SwitchComponent from "./Utils/Switch.jsx";
import getRequests from "./Utils/api/index.js";
import FlagBox from "./FlagBox.jsx";
import Logger from "./Logger.jsx";

const DUMMY_DATA = [
  { numberOfContainer: 1, numberOfBlocks: 30 },
  { numberOfContainer: 2, numberOfBlocks: 5 },
  { numberOfContainer: 3, numberOfBlocks: 7 },
];

const DUMMY_AUTOMAT_STATE = {
  containers: DUMMY_DATA,
  sensors: {
    1: { sensor_id: 1, sensor_name: "sensor1", sensor_value: 1 },
    2: { sensor_id: 2, sensor_name: "sensor2", sensor_value: 2 },
    3: { sensor_id: 3, sensor_name: "sensor3", sensor_value: 3 },
  },
  logged: false,
  user: "",
  mode: "manual",
  block: 0,
  working: false,
  belt_running: false,
  robort_working: false,
  photo_url: "https://picsum.photos/200/300",
};

const Monit = (props) => {
  const [automatState, setAutomatState] = useState(DUMMY_AUTOMAT_STATE);
  const [websocket, setWebsocket] = useState(null);
  const [logs, setLogs] = useState([]);

  const addLog = (log, logTime = null) => {
    const time = logTime ? logTime : new Date().getTime();

    const newLog = {
      id: uuidv4(),
      type: log.type,
      message: log.message,
      time: time,
    };
    console.log("new log", newLog);
    setLogs((prev) => [...prev, newLog]);
  };

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onopen = () => {
      console.log("Połączono z WebSocketem");
      setWebsocket(ws);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.event === "update") {
        setAutomatState((prev) => {
          if (prev.mode !== data.data.mode) {
            addLog({
              type: "info",
              message: `Zmieniono tryb pracy na ${data.data.mode}`,
            });
          }

          if (prev.working !== data.data.working) {
            // add log to logger
          }

          if (prev.belt_running !== data.data.belt_running) {
            // add log to logger
          }

          if (prev.robort_working !== data.data.robort_working) {
            // add log to logger
          }

          if (prev.block !== data.data.block) {
            // add log to logger
          }

          return {
            containers: data.data.containers,
            sensors: data.data.sensors,
            logged: data.data.logged,
            user: data.data.user,
            mode: data.data.mode,
            block: data.data.block,
            working: data.data.working,
            belt_running: data.data.belt_running,
            robort_working: data.data.robort_working,
            photo_url: data.data.photo_url,
          };
        });

        console.log("sensors", data.data.sensors);
      }
    };

    ws.onclose = () => {
      console.log("Rozłączono z WebSocketem");
      setWebsocket(null);
    };

    return () => {
      if (websocket) {
        websocket.close();
      }
    };
  }, []);

  // const onChangeMode = () => {
  //   console.log("change mode");
  //   if (automatState.mode === "manual") {
  //     getRequests.getModeRequest(1);
  //   } else {
  //     getRequests.getModeRequest(0);
  //   }
  // };

  const onChangeWorking = () => {
    console.log("change working");
    if (automatState.working) {
      getRequests.getStopRequest();
    } else {
      getRequests
        .getStartRequest()
        .then((res) => {
          console.log("response w fk", res);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };

  const sensorsFlags = Object.values(automatState.sensors).map((sensor) => {
    return { flag: sensor.sensor_value, label: sensor.sensor_name };
  });

  const allFlags = [
    ...sensorsFlags,
    { flag: automatState.working, label: "working" },
    { flag: automatState.belt_running, label: "belt_running" },
    { flag: automatState.robort_working, label: "robort_working" },
    { flag: automatState.logged, label: "logged" },
    { flag: automatState.mode === "auto", label: "Tryb Auto" },
    { flag: automatState.block, label: "block" },
  ];

  return (
    <>
      <nav className="nav">
        <div className="actions">
          {/* <SwitchComponent
            offStateString="Manual"
            onStateString="Auto"
            enable={true}
            onChange={onChangeMode}
            isSwitchOn={automatState.mode === "auto"}
          /> */}
          <SwitchComponent
            offStateString="STOP"
            onStateString="START"
            enable={true}
            onChange={onChangeWorking}
            isSwitchOn={automatState.working}
          />
        </div>

        <Button onClick={props.logout}>Wyloguj</Button>
      </nav>
      <div className="test">
        <FlagBox flags={allFlags} />
        <Logger logs={logs} />
      </div>
      <div className="container-container">
        <Container dane={automatState.containers[0]} />
        <Container dane={automatState.containers[1]} />
        <Container dane={automatState.containers[2]} />
      </div>
    </>
  );
};

Monit.propTypes = {
  logout: PropTypes.func.isRequired,
};

export default Monit;
