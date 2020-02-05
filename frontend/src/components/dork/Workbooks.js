import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";

import { getLeads } from "../../actions/dorks";

export class Workbooks extends Component {
  static PropTypes = {
    dorks: PropTypes.array.isRequired
  };

  render() {
    return (
      <div>
        <h1>Workbooks</h1>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  dorks: state.dorks.dorks
});

export default connect(mapStateToProps)(Workbooks);
