import PropTypes from "prop-types";

import "./Log.css";

const Log = ({ type, message, time }) => {
  const date = new Date(time);
  const timeString = date.toLocaleTimeString();

  if (type === "error") {
    return (
      <li className="log">
        {time} <span className="log-type error">{type}</span> {message}
      </li>
    );
  }
  console.log(typeof type);
  return (
    <li className="log">
      {timeString} <span className="log-type">{type}</span> {message}
    </li>
  );
};

Log.propTypes = {
  type: PropTypes.string.isRequired,
  message: PropTypes.string.isRequired,
  time: PropTypes.string.isRequired,
};

export default Log;
