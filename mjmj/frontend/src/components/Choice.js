import React, { Component } from 'react';

export class Choice extends Component {
  render() {
    return (
      <div className="choice-container">
        <div className="heading row">
          <p className="username col-6 text-end pe-0 fs-2 fw-bold">MiJin</p>
          <p className="col-6 text-start mt-1 ps-0 fs-4">'s pick</p>
        </div>
        <form className="choice">
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
            id="distance"
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
            id="price"
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
            id="traffic"
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
            id="facility"
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
            id="usability"
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

export default Choice;
