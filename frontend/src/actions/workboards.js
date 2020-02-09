import axios from "axios";

import { GET_WORKBOARDS, DELETE_WORKBOARD, ADD_WORKBOARD } from "./types";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";
// import workboard from "../reducers/workboard";
// import { Workboards } from "../components/workboard/Workboards";

// GET WORKBOARDS
export const getWorkboards = () => (dispatch, getState) => {
  axios
    .get("/api/dork/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_WORKBOARDS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// DELETE WORKBOARD
export const deleteWorkboard = id => (dispatch, getState) => {
  axios
    .delete(`/api/dork/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: DELETE_WORKBOARD,
        payload: id
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// ADD WORKBOARD
export const addWorkboard = workboard => (dispatch, getState) => {
  axios
    .post("/api/dork/", workboard, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addWorkboard: "workboard Added" }));
      dispatch({
        type: ADD_WORKBOARD,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
