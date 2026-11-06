#include <pybind11/pybind11.h>
#include "../include/PID.h"

namespace py = pybind11;

PYBIND11_MODULE(gnc, m) {

    m.doc() = "Python bindings for the PID";

    py::class_<gnc::PID>(m, "PID")

    .def(py::init<double, double, double, double>(),
        py::arg("kp"), py::arg("ki"), py::arg("kd"), py::arg("dt"))

    .def("run", &gnc::PID::run,
        py::arg("target"), py::arg("current"))

    .def("reset", &gnc::PID::reset);
    
}