import { combineReducers } from "redux";
import workboards from "./workboard";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  workboards,
  errors,
  messages,
  auth
});
