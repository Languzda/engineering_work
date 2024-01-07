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
  box_on_belt: false,
  prediction: false,
  working: false,
  belt_running: false,
  robort_working: false,
  photo_url: "https://picsum.photos/200/300",
};

const Monit = (props) => {
  const [automatState, setAutomatState] = useState(DUMMY_AUTOMAT_STATE);
  const [websocket, setWebsocket] = useState(null);
  const [logWebSocket, setLogWebSocket] = useState(null);
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
    const logWS = new WebSocket("ws://localhost:8000/ws/logs");

    logWS.onopen = () => {
      console.log("Połączono z LogWebSocketem");
      setLogWebSocket(logWS);
    };

    ws.onopen = () => {
      console.log("Połączono z WebSocketem");
      setWebsocket(ws);
    };

    logWS.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.event === "update") {
        console.log("log", data.data);
      }
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

          return {
            containers: data.data.containers,
            sensors: data.data.sensors,
            logged: data.data.logged,
            user: data.data.user,
            mode: data.data.mode,
            block: data.data.block,
            box_on_belt: data.data.box_on_belt,
            prediction: data.data.prediction,
            working: data.data.working,
            belt_running: data.data.belt_running,
            robort_working: data.data.robort_working,
            photo_url: data.data.photo_url,
          };
        });
      }
    };

    ws.onclose = () => {
      console.log("Rozłączono z WebSocketem");
      setWebsocket(null);
    };

    logWS.onclose = () => {
      console.log("Rozłączono z LogWebSocketem");
      setLogWebSocket(null);
    };

    return () => {
      if (websocket) {
        websocket.close();
      }
      if (logWebSocket) {
        logWebSocket.close();
      }
    };
  }, []);

  const onChangeMode = () => {
    console.log("change mode");
    if (automatState.mode === "manual") {
      getRequests.getModeRequest(1);
    } else {
      getRequests.getModeRequest(0);
    }
  };

  const onChangeWorking = () => {
    console.log("change working");
    if (automatState.working) {
      getRequests.getStopRequest();
    } else {
      getRequests.getStartRequest();
    }
  };

  const sensorsFlags = Object.values(automatState.sensors).map((sensor) => {
    return { flag: sensor.sensor_value, label: sensor.sensor_name };
  });

  const allFlags = [
    ...sensorsFlags,
    { flag: automatState.working, label: "System up" },
    { flag: automatState.belt_running, label: "Taśma w ruchu" },
    { flag: automatState.robort_working, label: "Robot w ruchu" },
    { flag: automatState.mode === "auto", label: "Tryb Auto" },
    { flag: automatState.box_on_belt, label: "Obiekt na taśmie" },
    { flag: automatState.prediction, label: "Predykcja" },
  ];

  const disableButtons =
    automatState.mode === "auto" || automatState.working === false
      ? true
      : false;

  return (
    <>
      <nav className="nav">
        <div className="actions">
          <SwitchComponent
            offStateString="Manual"
            onStateString="Auto"
            enable={true}
            onChange={onChangeMode}
            isSwitchOn={automatState.mode === "auto"}
          />
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
      <div className="buttons-tra">
        <Button
          disabled={disableButtons}
          className={"btn-tra"}
          onClick={() => getRequests.getMoveTrajectory(0)}
        >
          Wybierz pojemnik 1
        </Button>
        <Button
          disabled={disableButtons}
          className={"btn-tra"}
          onClick={() => getRequests.getMoveTrajectory(1)}
        >
          Wybierz pojemnik 2
        </Button>
        <Button
          disabled={disableButtons}
          className={"btn-tra"}
          onClick={() => getRequests.getMoveTrajectory(2)}
        >
          Wybierz pojemnik 3
        </Button>
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
