import { useState } from "react";

import LoginForm from "./components/LoginForm";
import Monit from "./components/Monit";
import getRequests from "./components/Utils/api";

import "./App.css";

function App() {
  const [isLogged, setIsLogged] = useState(false);

  const onLoginHandle = () => {
    if (isLogged) {
      getRequests.getLogoutRequest();
    }
    setIsLogged((prev) => !prev);
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
