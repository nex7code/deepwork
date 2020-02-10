import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addWorkboard } from "../../actions/workboards";

export class Form extends Component {
  state = {
    title: "",
    priority: "",
    description: ""
  };

  static propTypes = {
    addWorkboard: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { title, priority, description } = this.state;
    const workboards = { title, priority, description };
    this.props.addWorkboard(workboards);
    this.setState({
      title: "",
      priority: "",
      description: ""
    });
  };

  render() {
    const { title, priority, description } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Workboards</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Priority</label>
            <input
              className="form-control"
              type="text"
              name="priority"
              onChange={this.onChange}
              value={priority}
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea
              className="form-control"
              type="text"
              name="description"
              onChange={this.onChange}
              value={description}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addWorkboard })(Form);
