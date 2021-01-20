import React, { Component, Fragment } from 'react';

import Header from './layout/Header';
import Choice from './Choice';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Choice />
      </Fragment>
    );
  }
}

export default App;
