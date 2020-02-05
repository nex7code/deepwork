import React, { Fragment } from "react";
import Form from "./Form";
import Workboards from "./Workboards";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Workboards />
    </Fragment>
  );
}
