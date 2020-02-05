import React, { Fragment } from "react";
import Form from "./Form";
import Workbooks from "./Workbooks";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Workbooks />
    </Fragment>
  );
}
