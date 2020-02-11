import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getWorkboards, deleteWorkboard } from "../../actions/workboards";
// import workboards from "../../reducers/workboard";

export class Workboards extends Component {
  static propTypes = {
    workboards: PropTypes.array.isRequired,
    getWorkboards: PropTypes.func.isRequired,
    deleteWorkboard: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getWorkboards();
  }

  render() {
    return (
      <Fragment>
        <h2>Workboards</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Priority</th>
              <th>Description</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.workboards.map(workboard => (
              <tr key={workboard.id}>
                <td>{workboard.id}</td>
                <td>{workboard.title}</td>
                <td>{workboard.priority}</td>
                <td>{workboard.description}</td>
                <td>
                  <button
                    onClick={this.props.deleteWorkboard.bind(
                      this,
                      workboard.id
                    )}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  workboards: state.workboards.workboards
});

export default connect(mapStateToProps, { getWorkboards, deleteWorkboard })(
  Workboards
);
