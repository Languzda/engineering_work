import { useState } from "react";
import PropTypes from "prop-types";

import Container from "./Container.jsx";
import Button from "./Utils/Button.jsx";

import "./Monit.css";

const DUMMY_DATA = [
  { numberOfContainer: 1, numberOfBlocks: 30 },
  { numberOfContainer: 2, numberOfBlocks: 5 },
  { numberOfContainer: 3, numberOfBlocks: 7 },
];

const Monit = (props) => {
  const [state, setState] = useState(DUMMY_DATA);
  const [buttonsState, setButtonsState] = useState({
    start: false,
    stop: true,
  });

  const onStart = () => {
    if (buttonsState.start) return;
    console.log("start");
    setButtonsState({ start: true, stop: false });
  };

  const onStop = () => {
    if (buttonsState.stop) return;
    console.log("stop");
    setButtonsState({ start: false, stop: true });
  };
  console.log(state);

  return (
    <>
      <nav className="nav">
        Navigacja <Button onClick={props.logout}>Wyloguj</Button>
      </nav>
      <div className="test">
        <Button
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
        </Button>
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
