import axios from "axios";
import { stopSubmit } from "redux-form";

import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  LANGUAGE_CHANGED
} from "./types";

// REGISTER USER
export const register = ({ username, email, password }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({ username, email, password });

  try {
    const res = await axios.post("/api/auth/register", body, config);
    dispatch({
      type: REGISTER_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: REGISTER_FAIL
    });
    dispatch(stopSubmit("registerForm", err.response.data));
  }
};

// LOAD USER
export const loadUser = () => async (dispatch, getState) => {
  dispatch({ type: USER_LOADING });

  try {
    const res = await axios.get("/api/auth/user", tokenConfig(getState));
    dispatch({
      type: USER_LOADED,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: AUTH_ERROR
    });
  }
};

// LOGIN USER
export const login = ({ username, password }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({ username, password });

  try {
    const res = await axios.post("/api/auth/login", body, config);
    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL
    });
    dispatch(stopSubmit("loginForm", err.response.data));
  }
};

// LOGIN/CREATE SOCIAL USER
export const social_login = ({
  username,
  email,
  given_name,
  family_name,
  user_id,
  social_token,
  provider,
  image_url
}) => async dispatch => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({
    username,
    email,
    given_name,
    family_name,
    user_id,
    social_token,
    provider,
    image_url
  });

  try {
    const res = await axios.post("/api/auth/social_login", body, config);
    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL
    });
  }
};

// LOGOUT USER
export const logout = () => async (dispatch, getState) => {
  await axios.post("/api/auth/logout", null, tokenConfig(getState));
  dispatch({
    type: LOGOUT_SUCCESS
  });
};

// CHANGE USER LANGUAGE
export const change_language = (lang) => (dispatch) => {

  dispatch({
    type: LANGUAGE_CHANGED,
    payload: lang
  });
};


// helper function
export const tokenConfig = getState => {
  // Get token
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  return config;
};
