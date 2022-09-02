class Elements:
    def __init__(self, t_melting, t_boiling):
        self.t_melting = t_melting  # температура плавлення
        self.t_boiling = t_boiling  # температура кипіння

    def temperature_converter(self, t, measurement_scale):
        if measurement_scale == 'F':
            return int(round((t - 32) * 5 / 9))
        elif measurement_scale == 'K':
            return int(t - 273.15)
        elif measurement_scale == 'C':
            return int(t)

    def check_agg_state(self, t, measurement_scale):  # solid liquid gas
        t = self.temperature_converter(t, measurement_scale)
        if self.t_melting <= t <= self.t_boiling:
            return f"Element temperature - {t}_C\n\tAggregate state of the element -> liquid!\n"
        elif t < self.t_melting:
            return f"Element temperature - {t}_C\n\tAggregate state of the element -> solid!\n"
        else:
            return f"Element temperature - {t}_C\n\tAggregate state of the element -> gas!\n"


if __name__ == '__main__':
    iron = Elements(1538, 2862)
    print(iron.check_agg_state(3137, 'K'))
