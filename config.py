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
import imgaug.augmenters as iaa

def story_data():
    return GeneratorCfg(
        num_image=10,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=70,
            perspective_transform=UniformPerspectiveTransformCfg(12, 12, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "corpus" / "jp_text.txt"],
                    font_dir=CURRENT_DIR / "font",
                    font_size=(35, 68),
                    length=(20,39)
                ),
            ),
            # corpus_effects=Effects(Line(0.2, thickness=(2, 5),line_pos_p=(0, 1, 0, 0, 0, 0, 0, 0, 0, 0))),  #Underline
            corpus_effects=Effects(ImgAugEffect(p=1,aug=iaa.GaussianBlur(sigma=(1.35, 1.35)))),   #Gaussian Blur
            # corpus_effects=Effects(Padding(p=1, w_ratio=[0.015, 0.021], h_ratio=[0.3, 0.35], center=True)), #Add padding
            gray=False,
            text_color_cfg=SimpleTextColorCfg(),
        ),
    )

configs = [story_data()]
