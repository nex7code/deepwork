import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";

import { getWorkboards } from "../../actions/workboards";

export class Workboards extends Component {
  static PropTypes = {
    workboards: PropTypes.array.isRequired
  };

  render() {
    return (
      <div>
        <h1>Workboards</h1>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  workboards: state.workboards.workboards
});

export default connect(mapStateToProps)(Workboards);
