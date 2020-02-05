import axios from "axios";

import { GET_DORKS } from "./types";

// GET DORKS
export const getDorks = () => dispatch => {
  axios
    .get("/api/dork/")
    .then(res => {
      dispatch({
        type: GET_DORKS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};
