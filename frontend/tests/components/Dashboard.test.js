import { render, screen } from "@testing-library/react";
import Dashboard from "../../src/components/Dashboard";

test("renders Dashboard component", () => {
  render(<Dashboard />);
  expect(screen.getByText(/Dashboard/i)).toBeInTheDocument();
});
