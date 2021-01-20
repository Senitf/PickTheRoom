import React, { Component } from 'react';

export class Header extends Component {
  render() {
    return (
      <nav class="navbar navbar-expand navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            MnM
          </a>
          <ul class="navbar-nav justify-content-end">
            <li class="nav-item">
              <a class="nav-link" href="#">
                Login
                <i className="fas fa-sign-in-alt"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <i className="fas fa-star"></i>
              </a>
            </li>
          </ul>
        </div>
      </nav>
    );
  }
}

export default Header;
