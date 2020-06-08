from math import sin, cos, pi


class Sun:
    def __init__(self, zenit_height, angle, procession_speed):
        self.zenit_height = zenit_height
        self.angle = angle  # initialized in radians
        self.procession_speed = procession_speed
        self.curr_height = zenit_height * sin(angle)
        self.curr_x1 = zenit_height * cos(angle)  # relative to the center
        self.x2 = 0  # the Sun is always passing through the middle of the Earth
        self.shedding_light = True if 0 < angle < pi else False

    def move(self, time_elapsed):
        self.angle = self.angle + self.procession_speed * time_elapsed
        self.curr_height = self.zenit_height * sin(self.angle)
        self.curr_x1 = self.zenit_height *     cos(self.angle)

    def is_shedding_light(self):
        if 0 < (self.angle % (2 * pi)) < 2 * pi:
            self.shedding_light = True
            return True
        else:
            self.shedding_light = False
            return False

    def days_passed(self):
        days = self.angle // (2 * pi)
        return days


class Cloud:
    def __init__(self, height, form, x1, x2, speed_x1, speed_x2, vertical_speed):
        self.height = height
        self.form = form
        self.x1 = x1
        self.x2 = x2
        self.speed_x1 = speed_x1
        self.speed_x2 = speed_x2
        self.vertical_speed = vertical_speed

    def move(self, time_elapsed):
        self.height += self.vertical_speed * time_elapsed
        self.x1 = self.x1 + self.speed_x1 * time_elapsed
        self.x2 = self.x2 + self.speed_x2 * time_elapsed


class TerrestrialObserver:
    def __init__(self, x1, x2, altitude, consider_to_be_cloud, consider_to_be_sky):
        self.observers_x1 = x1
        self.observers_x2 = x2
        self.altitude = altitude
        self.consider_to_be_cloud = consider_to_be_cloud
        self.consider_to_be_sky = consider_to_be_sky

    def is_sunny(self, sun, cloud):

        def is_cloud(segment):
            if segment == self.consider_to_be_cloud:

                return True
            elif segment == self.consider_to_be_sky:
                return False

        if not sun.is_shedding_light():
            return False

        else:
            if cloud.height >= sun.curr_height and sun.shedding_light:
                # it does no happen in reality
                return True

            elif self.altitude > cloud.height and sun.shedding_light:
                return True

            else:
                for x1, strip in enumerate(cloud.form):
                    for x2, picture_segment in enumerate(strip):
                        if is_cloud(picture_segment):
                            # relative to Earth
                            rel_e_x1 = cloud.x1 + x1
                            rel_e_x2 = cloud.x2 + x2

                            k = sun.curr_height / (sun.curr_height - cloud.height)
                            cloud_width = 1  # the width of one segment

                            if sun.curr_x1 == rel_e_x1:
                                x1_shadow_lbound = rel_e_x1 - cloud_width / 2 * k
                                x1_shadow_rbound = rel_e_x1 + cloud_width / 2 * k

                            elif sun.curr_x1 > rel_e_x1:
                                center_displacement = sun.curr_x1 - rel_e_x1
                                x1_shadow_lbound = center_displacement - cloud_width / 2 * k
                                x1_shadow_rbound = center_displacement + cloud_width / 2 * k

                            else:
                                center_displacement = rel_e_x1 - sun.curr_x1
                                x1_shadow_lbound = center_displacement - cloud_width / 2 * k
                                x1_shadow_rbound = center_displacement + cloud_width / 2 * k

                            on_the_same_x1 = (x1_shadow_lbound <= self.observers_x1 <= x1_shadow_rbound)
                            on_the_same_x2 = ((rel_e_x2 - cloud_width/2) <= self.observers_x2 <= (rel_e_x2 + cloud_width/2))

                            if on_the_same_x1 and on_the_same_x2:
                                return False
        return True


