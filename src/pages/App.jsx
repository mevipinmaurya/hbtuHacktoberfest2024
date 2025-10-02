import { Routes, Route } from "react-router-dom";
import NotFound from "./pages/NotFound";

<Routes>
  {/* your other routes here */}
  <Route path="*" element={<NotFound />} />
</Routes>
