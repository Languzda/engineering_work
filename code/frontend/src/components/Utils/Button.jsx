import PropTypes from "prop-types";
import "./Button.css";

const Button = (props) => {
  const classes = `btn ${props.className}`;

  return (
    <button className={classes} onClick={props.onClick}>
      {props.children}
    </button>
  );
};

Button.propTypes = {
  onClick: PropTypes.func,
  children: PropTypes.node.isRequired,
  className: PropTypes.string,
};

export default Button;
