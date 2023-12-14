import { useState, useEffect } from "react";
import PropTypes from "prop-types";

import Container from "./Container.jsx";
import Button from "./Utils/Button.jsx";

import "./Monit.css";
import SwitchComponent from "./Utils/Switch.jsx";
import getRequests from "./Utils/api/index.js";

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
  const [state, setState] = useState(DUMMY_DATA);
  const [websocket, setWebsocket] = useState(null);
  const [buttonsState, setButtonsState] = useState({
    start: false,
    stop: true,
  });

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onopen = () => {
      console.log("Połączono z WebSocketem");
      setWebsocket(ws);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      // console.log("Otrzymano dane RAW z WebSocket:", data);
      if (data.event === "update") {
        // console.log("Otrzymano dane UPDATE z WebSocket:", data.data);
        setAutomatState({
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
        });
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

  // const onStart = () => {
  //   if (buttonsState.start) return;
  //   console.log("start");
  //   setButtonsState({ start: true, stop: false });
  // };

  // const onStop = () => {
  //   if (buttonsState.stop) return;
  //   console.log("stop");
  //   setButtonsState({ start: false, stop: true });
  // };

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
        {/* <Button
          onClick={onStart}
          className={`btn-control ${
            buttonsState.start ? "btn-active-start" : "btn-start"
          }`}
        >
          START
        </Button>
        <Button
          onClick={onStop}
          className={`btn-control ${
            buttonsState.stop ? "btn-active-stop" : "btn-stop"
          }`}
        >
          STOP
        </Button> */}
      </div>
      <div className="container-container">
        <Container dane={state[0]} />
        <Container dane={state[1]} />
        <Container dane={state[2]} />
      </div>
    </>
  );
};

Monit.propTypes = {
  logout: PropTypes.func.isRequired,
};

export default Monit;
