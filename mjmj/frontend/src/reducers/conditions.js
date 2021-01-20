import { GET_CONDITIONS, ADD_CONDITION } from '../actions/types.js';

const initialState = {
  conditions: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_CONDITIONS:
      return {
        ...state,
        conditions: action.payload,
      };
    case ADD_CONDITION:
      return {
        ...state,
        conditions: [...state.conditions, action.payload],
      };
    default:
      return state;
  }
}
