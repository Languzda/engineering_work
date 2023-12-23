import PropTypes from "prop-types";

import "./FlagBox.css";

import Flag from "./flag";

const FlagBox = ({ flags }) => {
  return (
    <div className="flag-box">
      <div className="flag-box-header">Stany:</div>
      <div className="flag-box-flags">
        {flags.map((flag) => (
          <Flag key={flag.label} flag={flag.flag} label={flag.label} />
        ))}
      </div>
    </div>
  );
};

FlagBox.propTypes = {
  flags: PropTypes.arrayOf(
    PropTypes.shape({
      flag: PropTypes.bool.isRequired,
      label: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default FlagBox;
