import {
  GET_WORKBOARDS,
  DELETE_WORKBOARD,
  ADD_WORKBOARD
} from "../actions/types";

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
    case DELETE_WORKBOARD:
      return {
        ...state,
        workboards: state.workboards.filter(
          workboard => workboard.id !== action.payload
        )
      };
    case ADD_WORKBOARD:
      return {
        ...state,
        workboards: [...state.workboards, action.payload]
      };
    default:
      return state;
  }
}
