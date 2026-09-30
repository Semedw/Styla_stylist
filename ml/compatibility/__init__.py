"""Styla A Compatibility & Ranking Modulu (Rol A).

Geyim cAtlTrinin vizual vT stil uyYunluYunu (compatibility) qiymTtlTndirTn
PyTorch modellTri, tTlim skriptlTri vT sArTtli scoring funksiyalar.

ctimai API:
    from ml.compatibility import (
        CompatibilityMLP,
        CompatibilityScorer,
        score_compatibility,
        score_compatibility_batch,
        train_compatibility_model,
    )

Qeyd: `config` vT `rules` birbaSa import olunur (yungul — numpy/PIL),
qalanlari lazy — `import ml.compatibility` sklearn/torch-u yuklTmir,
eks halda serve image (requirements-serve.txt) `from sklearn...`
xTtasinda cökur. Pattern ucun bax: `ml/retrieval/__init__.py`.
"""
from ml.compatibility import config
from ml.compatibility.rules import color_clash, hue_distance, is_neutral, pattern_clash

__all__ = [
    "config",
    "CompatibilityMLP",
    "TypeAwareCompatibilityModel",
    "PairCompatibilityDataset",
    "create_pairs_from_outfits",
    "load_pairs_from_npz",
    "save_pairs_to_npz",
    "split_dataset",
    "get_dataloaders",
    "CompatibilityScorer",
    "get_scorer",
    "score_compatibility",
    "score_compatibility_batch",
    "train_compatibility_model",
    "CATEGORIES",
    "Outfit",
    "WardrobeItem",
    "generate_outfit",
    "outfit_is_valid",
    "color_clash",
    "hue_distance",
    "is_neutral",
    "pattern_clash",
]


def __getattr__(name: str):
    """Lazy import — agir modulometries yalniz istifade olunanda yuklenir.

    `train` xususi il sklearn (dev-only) cekir; `model`/`dataset`/`scorer`
    torch cekir. Serve-da `from ml.compatibility.rules import ...` artiq
    bunlari cekmir.
    """
    if name in ("CompatibilityMLP", "TypeAwareCompatibilityModel"):
        from ml.compatibility import model

        return getattr(model, name)
    if name in (
        "PairCompatibilityDataset",
        "create_pairs_from_outfits",
        "load_pairs_from_npz",
        "save_pairs_to_npz",
        "split_dataset",
        "get_dataloaders",
    ):
        from ml.compatibility import dataset

        return getattr(dataset, name)
    if name in (
        "CompatibilityScorer",
        "get_scorer",
        "score_compatibility",
        "score_compatibility_batch",
    ):
        from ml.compatibility import scorer

        return getattr(scorer, name)
    if name == "train_compatibility_model":
        from ml.compatibility.train import train_compatibility_model

        return train_compatibility_model
    if name in (
        "CATEGORIES",
        "Outfit",
        "WardrobeItem",
        "generate_outfit",
        "outfit_is_valid",
    ):
        from ml.compatibility import generate

        return getattr(generate, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
