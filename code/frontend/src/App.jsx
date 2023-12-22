import { useState } from "react";

import LoginForm from "./components/LoginForm";
import Monit from "./components/Monit";
import getRequests from "./components/Utils/api";

import "./App.css";

function App() {
  const [isLogged, setIsLogged] = useState(
    localStorage.getItem("isLogged")
      ? localStorage.getItem("isLogged") === "true"
      : false
  );

  const onLoginHandle = () => {
    if (isLogged) {
      getRequests.getLogoutRequest();
    }
    setIsLogged((prev) => {
      localStorage.setItem("isLogged", !prev);
      return !prev;
    });
  };

  return (
    <div className="app">
      {isLogged ? (
        <Monit logout={onLoginHandle} />
      ) : (
        <LoginForm onlogin={onLoginHandle} />
      )}
    </div>
  );
}

export default App;
