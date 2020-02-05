import axios from "axios";

import { GET_WORKBOARDS } from "./types";

// GET WORKBOARDS
export const getWorkboards = () => dispatch => {
  axios
    .get("/api/dork/")
    .then(res => {
      dispatch({
        type: GET_WORKBOARDS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};
