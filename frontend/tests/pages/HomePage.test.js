import { render, screen } from "@testing-library/react";
import HomePage from "../../src/pages/HomePage";

test("renders HomePage component", () => {
  render(<HomePage />);
  expect(screen.getByText(/Welcome to Smart Data Dashboard/i)).toBeInTheDocument();
});
