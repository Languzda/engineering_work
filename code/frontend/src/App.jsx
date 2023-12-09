import { useState } from "react";

import LoginForm from "./components/LoginForm";
import Monit from "./components/Monit";

import "./App.css";

function App() {
  const [isLogged, setIsLogged] = useState(false);

  const onLoginHandle = () => {
    console.log(isLogged);
    setIsLogged((prev) => !prev);
  };

  return (
    <div className="app">
      {isLogged ? (
        <Monit logout={onLoginHandle} />
      ) : (
        <LoginForm login={onLoginHandle} />
      )}
    </div>
  );
}

export default App;
