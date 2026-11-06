#include "../include/PID.h"

namespace gnc {
    PID::PID(double kp, double ki, double kd, double dt) {
        kpP = kp;
        kiP = ki;
        kdP = kd;
        dtP = dt;
        integralSumP = 0;
        previousErrorP = 0;
    }

    double PID::run(double target, double current) {

        double error = target - current;

        double pGain = kpP * error;

        integralSumP += error * dtP;
        double iGain = kiP * integralSumP;

        double derivative = (error - previousErrorP) / dtP;
        double dGain = kdP * derivative;

        previousErrorP = error;

        return pGain + iGain + dGain;

    }

    void PID::reset() {
        integralSumP = 0;
        previousErrorP = 0;
    }
}
