import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addCondition } from '../actions/conditions';

export class Choice extends Component {
  state = {
    distance: 0,
    price: 0,
    traffic: 0,
    facility: 0,
    usability: 0,
  };

  static PropTypes = {
    addCondition: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { distance, price, traffic, facility, usability } = this.state;
    const condition = { distance, price, traffic, facility, usability };
    this.props.addCondition(condition);
    this.setState({
      distance: 0,
      price: 0,
      traffic: 0,
      facility: 0,
      usability: 0,
    });
  };

  render() {
    const { distance, price, traffic, facility, usability } = this.state;

    return (
      <div className="choice-container">
        <div className="heading row">
          <p className="username col-6 text-end pe-0 fs-2 fw-bold">MiJin</p>
          <p className="col-6 text-start mt-1 ps-0 fs-4">'s pick</p>
        </div>
        <form className="choice" onSubmit={this.onSubmit}>
          <label className="mb-0" for="distance">
            거리<i className="far fa-question-circle"></i>
          </label>
          <input
            type="range"
            className="form-range"
            min="0"
            max="5"
            step="1"
            defaultValue="0"
            onChange={this.onChange}
            name="distance"
          />
          <label className="mb-0" for="price">
            가격<i className="far fa-question-circle"></i>
          </label>
          <input
            type="range"
            className="form-range"
            min="0"
            max="5"
            step="1"
            defaultValue="0"
            onChange={this.onChange}
            name="price"
          />
          <label className="mb-0" for="traffic">
            교통<i className="far fa-question-circle"></i>
          </label>
          <input
            type="range"
            className="form-range"
            min="0"
            max="5"
            step="1"
            defaultValue="0"
            onChange={this.onChange}
            name="traffic"
          />
          <label className="mb-0" for="facility">
            상업시설<i className="far fa-question-circle"></i>
          </label>
          <input
            type="range"
            className="form-range"
            min="0"
            max="5"
            step="1"
            defaultValue="0"
            onChange={this.onChange}
            name="facility"
          />
          <label className="mb-0" for="usability">
            편의성<i className="far fa-question-circle"></i>
          </label>
          <input
            type="range"
            className="form-range"
            min="0"
            max="5"
            step="1"
            defaultValue="0"
            onChange={this.onChange}
            name="usability"
          />
          <div class="d-grid gap-2 mt-2 mb-0">
            <button className="btn btn-primary btn-lg" type="submit">
              Search
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addCondition })(Choice);
