#ifndef AEROGNC_PID_H
#define AEROGNC_PID_H

namespace gnc {

    class PID {
    public:
        PID(double kp, double ki, double kd, double dt);

        double run(double target, double current);

        void reset();

    private:
        double kpP;
        double kiP;
        double kdP;
        double dtP;
        double integralSumP;
        double previousErrorP;

    };

}

#endif //AEROGNC_PID_H
