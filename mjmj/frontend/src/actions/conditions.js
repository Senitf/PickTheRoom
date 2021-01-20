import axios from 'axios';

import { GET_CONDITIONS, ADD_CONDITION, SEARCH } from './types';

// GET_CONDITIONS
export const getConditions = () => (dispatch) => {
  axios
    .get('/api/conditions/')
    .then((res) => {
      dispatch({
        type: GET_CONDITIONS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};

// ADD_CONDITION
export const addCondition = (condition) => (dispatch) => {
  axios
    .post('/api/conditions/', condition)
    .then((res) => {
      dispatch({
        type: ADD_CONDITION,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};

// SEARCH
export const search = (condition) => (dispatch) => {
  axios
    .get('/api/conditions')
    .then((res) => {
      dispatch({
        type: SEARCH,
        payload: condition,
      });
    })
    .catch((err) => console.log(err));
};
