import "./LoginForm.css";
import getRequests from "./Utils/api";

import PropTypes from "prop-types";

function LoginForm({ onlogin }) {
  const sumbitHandler = async (event) => {
    event.preventDefault();

    const login = event.target.login.value;
    const password = event.target.password.value;

    if (login === "" || password === "") {
      alert("Nie podano loginu lub hasła");
      return;
    }

    const data = await getRequests.getLoginRequest(login, password);

    if (data.message === "OK") {
      onlogin();
    } else {
      alert("Niepoprawny login lub hasło");
    }
  };

  return (
    <div className="loginFormBox" onSubmit={sumbitHandler}>
      <h1 className="header">Zaloguj się do Panelu</h1>
      <form className="loginForm">
        <label htmlFor="login">Nazwa użytkownika</label>
        <input type="text" name="login" />
        <label htmlFor="password">Hasło</label>
        <input type="password" name="password" />
        <input type="submit" value="Zaloguj" />
      </form>
    </div>
  );
}

LoginForm.propTypes = {
  onlogin: PropTypes.func.isRequired,
};

export default LoginForm;
