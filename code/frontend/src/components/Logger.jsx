import "./Logger.css";
import Log from "./Log";
import PropTypes from "prop-types";
import { v4 as uuidv4 } from "uuid";

const Logger = ({ logs }) => {
  const sortedLogs = logs.sort((a, b) => b.time - a.time);
  return (
    <div className="logger">
      <h3 className="logger-header">Logi:</h3>
      <ul className="logger-list">
        {sortedLogs.map((log) => {
          console.log(log);
          return (
            <Log
              key={uuidv4()}
              type={log.type}
              message={log.message}
              time={log.time}
            />
          );
        })}
      </ul>
    </div>
  );
};

Logger.propTypes = {
  logs: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      type: PropTypes.string.isRequired,
      message: PropTypes.string.isRequired,
      date: PropTypes.instanceOf(Date).isRequired,
    })
  ).isRequired,
};

export default Logger;
