---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
---
<!-- theme: uncover -->

![bg left:40% 80%](https://raw.githubusercontent.com/marp-team/marp/master/marp.png)

# **Marp**

Markdown Presentation Ecosystem

https://marp.app/

---

# How to write slides

Split pages by horizontal ruler (`---`). It's very simple! :satisfied:

```markdown
# Slide 1

foobar

---

# Slide 2

foobar
```

---

# Test code

```python
# This method is used in 2007.
def voc_ap(rec, prec): 
    ap = 0.
    for t in np.arange(0., 1.1, 0.1):
        if np.sum(rec >= t) == 0:
            p = 0
        else:
            p = np.max(prec[rec >= t])
        ap = ap + p / 11.
    return ap
```
---

# Test of latex equation

$OKS = \frac{\sum_{i}[\exp (\frac{-d_i^2 }{2S^2K_i^2})
\delta(\textup{v}_i>0)]}{\sum_{i}[\delta(\textup{v}_i>0)]}$
