const apiURL = "http://localhost:8000/";

export const getAutomatState = async () => {
  const response = await fetch(`${apiURL}state`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

export const getStopRequest = async () => {
  const response = await fetch(`${apiURL}stop`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

export const getStartRequest = async () => {
  const response = await fetch(`${apiURL}start`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

export const getLogoutRequest = async () => {
  const response = await fetch(`${apiURL}logout`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

export const getLoginRequest = async (user, password) => {
  const response = await fetch(`${apiURL}login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user, password }),
  });

  if (!response.ok) {
    console.log("Login failed");
  }

  const data = await response.json();
  return data;
};

export const getModeRequest = async (mode) => {
  const response = await fetch(`${apiURL}mode/${mode}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

export const getMoveTrajectory = async (trajectory) => {
  const response = await fetch(`${apiURL}trajectory/${trajectory}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};
