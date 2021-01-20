import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getConditions } from '../actions/conditions';

export class Result extends Component {
  static PropTypes = {
    conditions: PropTypes.array.isRequired,
    getConditions: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getConditions();
  }

  render() {
    return (
      <Fragment>
        <h1>Result</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>거리</th>
              <th>가격</th>
              <th>교통</th>
              <th>상업시설</th>
              <th>편의성</th>
            </tr>
          </thead>
          <tbody>
            {this.props.conditions.map((condition) => (
              <tr key={condition.id}>
                <td>{condition.distance}</td>
                <td>{condition.price}</td>
                <td>{condition.traffic}</td>
                <td>{condition.facility}</td>
                <td>{condition.usability}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  conditions: state.conditions.conditions,
});

export default connect(mapStateToProps, { getConditions })(Result);
