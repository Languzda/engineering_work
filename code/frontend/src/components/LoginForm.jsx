import "./LoginForm.css";

function LoginForm(props) {
  return (
    <div className="loginFormBox">
      <h1 className="header">Zaloguj się do Panelu</h1>
      <form className="loginForm">
        <label htmlFor="login">Nazwa użytkownika</label>
        <input type="text" name="login" />
        <label htmlFor="password">Hasło</label>
        <input type="password" name="password" />
        <button onClick={props.login}>Zaloguj</button>
      </form>
    </div>
  );
}

export default LoginForm;
