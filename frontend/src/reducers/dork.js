import { GET_DORKS } from "../actions/types";

const initialState = {
  dorks: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_DORKS:
      return {
        ...state,
        dorks: action.payload
      };
    default:
      return state;
  }
}
