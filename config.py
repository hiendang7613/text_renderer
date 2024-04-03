import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    SimpleTextColorCfg,
    UniformPerspectiveTransformCfg,
)

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))


def story_data():
    return GeneratorCfg(
        num_image=10,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=32,
            perspective_transform=UniformPerspectiveTransformCfg(12, 12, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "corpus" / "jp_text.txt"],
                    font_dir=CURRENT_DIR / "font",
                    font_size=(20, 30),
                    length=(3,39)
                ),
            ),
            corpus_effects=Effects(Line(0.5, thickness=(2, 5),line_pos_p=(0, 1, 0, 0, 0, 0, 0, 0, 0, 0))),
            gray=False,
            text_color_cfg=SimpleTextColorCfg(),
        ),
    )


configs = [story_data()]
