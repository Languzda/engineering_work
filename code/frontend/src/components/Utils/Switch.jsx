import "./Switch.css";

import PropTypes from "prop-types";

const SwitchComponent = ({
  onStateString,
  offStateString,
  enable = true,
  onChange,
  isSwitchOn,
}) => {
  const handleToggle = () => {
    if (enable) {
      onChange();
    }
  };

  return (
    <div className={`switch-container ${enable ? "" : "disabled"}`}>
      <span className="switch-label">{offStateString}</span>
      <label className={`switch ${enable ? "" : "disabled"}`}>
        <input
          type="checkbox"
          checked={isSwitchOn}
          onChange={handleToggle}
          disabled={!enable}
        />
        <span className="slider round"></span>
      </label>
      <span className="switch-label">{onStateString}</span>
    </div>
  );
};

SwitchComponent.propTypes = {
  onStateString: PropTypes.string.isRequired,
  offStateString: PropTypes.string.isRequired,
  enable: PropTypes.bool,
  onChange: PropTypes.func.isRequired,
  isSwitchOn: PropTypes.bool,
};

export default SwitchComponent;
