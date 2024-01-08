import { useState } from "react";
import LoginForm from "./components/LoginForm";
import Monit from "./components/Monit";
import getRequests from "./components/Utils/api";

import "./App.css";

function App() {
  const [isLogged, setIsLogged] = useState(async () => {
    const response = await getRequests.getAutomatState();
    const state = response.data.logged;
    console.log("state", state);
    return state;
  });

  const onLoginHandle = async () => {
    if (isLogged) {
      await getRequests.getLogoutRequest();
    } else {
      await getRequests.getLoginRequest();
    }

    setIsLogged((prev) => {
      console.log("prev", prev);
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
