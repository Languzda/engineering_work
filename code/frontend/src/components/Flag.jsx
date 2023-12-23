import PropTypes from "prop-types";

import "./Flag.css";

const Flag = ({ flag, label }) => {
  return (
    <div className="flag">
    <div className={`flag-status ${flag ? "active" : ""}`}></div>
      <div>{label}</div>
    </div>
  );
};

Flag.propTypes = {
  flag: PropTypes.bool.isRequired,
  label: PropTypes.string.isRequired,
};

export default Flag;
