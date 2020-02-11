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
        {/* <h2>Add Workboards</h2> */}
        <form onSubmit={this.onSubmit} className="form-row">
          <div className="col col-md-4">
            {/* <label>Title</label> */}
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
              placeholder="Title"
            />
          </div>
          <div className="col col-md-4">
            {/* <label>Priority</label> */}
            <input
              className="form-control-range"
              type="range"
              name="priority"
              onChange={this.onChange}
              value={priority}
              // placeholder="Priority"
            />
          </div>
          <div className="col col-md-4">
            {/* <label>Description</label> */}
            <input
              className="form-control"
              type="text"
              name="description"
              onChange={this.onChange}
              value={description}
              placeholder="Description"
            />
          </div>
          <div className="col">
            <input
              button
              type="submit"
              className="btn btn-primary"
              Submit
              hidden
            />
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addWorkboard })(Form);
