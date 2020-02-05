import { GET_WORKBOARDS } from "../actions/types";

const initialState = {
  workboards: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_WORKBOARDS:
      return {
        ...state,
        workboards: action.payload
      };
    default:
      return state;
  }
}
