from manimlib import *


class MultiHeadedAttention(InteractiveScene):
    def construct(self):
        n_heads = 4
        heads = Group()
        for n in range(n_heads):
            im = ImageMobject("assets/prompt.png").set_opacity(1).shift(0.01 * OUT)
            # rect = SurroundingRectangle(im, buff=0.0).set_fill(BLACK, 0.75).set_stroke(WHITE, 1, 1)
            heads.add(im)

        heads.set_height(4).arrange(OUT, buff=2.0).move_to(DOWN)

        pre_head = ImageMobject("assets/prompt.png").move_to(4 * LEFT)
        self.set_floor_plane("xz")
        self.add(pre_head)
        self.wait()
        self.play(
            self.frame.animate.reorient(41, -12, 0, (-1.0, -1.42, 1.09), 12.90).set_anim_args(run_time=2),
            FadeTransform(pre_head, heads[-1], time_span=(1, 2)),
        )

        self.play(
            self.frame.animate.reorient(48, -11, 0, (-1.0, -1.42, 1.09), 12.90),
            LaggedStart((FadeTransform(heads[-1].copy(), image) for image in heads),
                        lag_ratio=0.1,
                        group_type=Group,
                        ),
            run_time=4,
        )