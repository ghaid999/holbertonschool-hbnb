# HBnB Evolution - Technical Documentation

## Table of Contents

1. Introduction
2. High-Level Architecture
3. Business Logic Layer
4. API Interaction Flow
5. Conclusion

---

# 1. Introduction

## Purpose

> Write a brief explanation of the purpose of this document.

## Project Overview

> Briefly describe the HBnB Evolution application and its objectives.

## Scope

> Explain what this document covers.

---

# 2. High-Level Architecture

## Overview

> Explain the layered architecture used in the project.

### Package Diagram

*(Insert the Package Diagram here.)*

### Presentation Layer

> Explain its responsibilities.

### Business Logic Layer

> Explain its responsibilities.

### Persistence Layer

> Explain its responsibilities.

### Facade Pattern

> Explain why the Facade pattern is used and how it connects the layers.

---

# 3. Business Logic Layer

## Overview

> The foolweng digram that explan the whol system inside the Business Logic Layer

### Class Diagram

*(Insert the Class Diagram here.)*

---

## BaseEntity

### Role

> The BaseEntity is the class that contain the atributs that is commen in all other class,so all the class inheret from BaseEntity. 

### Attributes

- id
- created_at
- updated_at

---

## User

### Role

> The user class is themain class , in this class the user can register, update , and delete .

### Attributes

- first_name
- last_name
- email
- password
- is_admin

### Methods

- register(first_name, last_name, email, password) : void
- update_profile(id, data) : void
- delete(id) : void

---

## Place

### Role

> in class place we have the information about the plece.

### Attributes

- title
- description
- price
- latitude
- longitude

### Methods

- create(title, description, price, latitude, longitude, owner_id) : void
- update(id, data) : void
- delete(id) : void
- list_all() : List<Place>
- add_amenity(amenity_id) : void
- remove_amenity(amenity_id) : void

---

## Review

### Role

> in class Review , a user can write a review , and a place have a reviews about the place.

### Attributes

- rating
- comment

### Methods

- create(place_id, user_id, rating, comment) : void
- update(id, data) : void
- delete(id) : void
- list_by_place(place_id) : List<Review>

---

## Amenity

### Role

> class Amenity , is the class that contain the Amenity about the place.

### Attributes

- name
- description

### Methods

- create(name, description) : void
- update(id, data) : void
- delete(id) : void
- list_all() : List<Amenity>

---

## Relationships

### BaseEntity → Entities

> The atruputs that share in all the Entities.

### User → Place

> A user can have multible places.

### User → Review

> A user can write multible Reviews about the places.

### Place → Review

> A place can have multible review that writen by the user.

### Place ↔ Amenity

> A place can have multible Amenity.

---

# 4. API Interaction Flow

## Overview

> Briefly explain what the sequence diagrams represent.

---

## User Registration

[![](https://mermaid.ink/img/pako:eNp9U8Fu2zAM_RWBl22AE8RJXCc6BNhaDAiwDkWL7jD4wtmMK8CWPEkO1gX591FOnMVNNl0smu-RjxS5g9wUBBIc_WxJ53SnsLRYZzbTgg_m3ljx7Mj2fxq0XuWqQe3Fx4f1td-fWqc0OffFlCq_BrhDjz_QUfD1_sqYRjxrr6rOLb5hpYreGU4QMVqtOKcUj1Qq5y16ZTQbLN35cyyDGDrQIQ8R0ZNAXYgHa3J2XSOf37E6qBVfjb-UFM4gyagXuNbbAO64bxlBHONCPVLcMxVLEhms_TsnNKfZHnUWkWgq4jYJb18Flqh0BufBSJ_UHK-9ORS1WvUNl-IJtzRQdaX_ATOos6ePLpvaxfuMqhoy_i3gkUI1FzLOaum__8l6a_RG2boLc73mv5PiWxtmxDVGuxN48AZvpumAFO-f2jyMyAeIoLSqAOltSxHUZGsMJuxCrAz8C9WUgeRrQRtsK8_PpPdM42H_bkzdM61pyxeQG6wcW20THvm4bycI94HsrWm1Bxkniy4GyB38AjlNJ-PZzewmSdPZfB4vkiSCV5DJYpywNZkt59MkWcb7CH53SSfjNI2niziepstkPkmXEVCheJ_vDyvfbf7-DyJQR1E?type=png)](https://mermaid.live/view#pako:eNp9U8Fu2zAM_RWBl22AE8RJXCc6BNhaDAiwDkWL7jD4wtmMK8CWPEkO1gX591FOnMVNNl0smu-RjxS5g9wUBBIc_WxJ53SnsLRYZzbTgg_m3ljx7Mj2fxq0XuWqQe3Fx4f1td-fWqc0OffFlCq_BrhDjz_QUfD1_sqYRjxrr6rOLb5hpYreGU4QMVqtOKcUj1Qq5y16ZTQbLN35cyyDGDrQIQ8R0ZNAXYgHa3J2XSOf37E6qBVfjb-UFM4gyagXuNbbAO64bxlBHONCPVLcMxVLEhms_TsnNKfZHnUWkWgq4jYJb18Flqh0BufBSJ_UHK-9ORS1WvUNl-IJtzRQdaX_ATOos6ePLpvaxfuMqhoy_i3gkUI1FzLOaum__8l6a_RG2boLc73mv5PiWxtmxDVGuxN48AZvpumAFO-f2jyMyAeIoLSqAOltSxHUZGsMJuxCrAz8C9WUgeRrQRtsK8_PpPdM42H_bkzdM61pyxeQG6wcW20THvm4bycI94HsrWm1Bxkniy4GyB38AjlNJ-PZzewmSdPZfB4vkiSCV5DJYpywNZkt59MkWcb7CH53SSfjNI2niziepstkPkmXEVCheJ_vDyvfbf7-DyJQR1E)


### Description 

> Explain the flow.

---

## Place Creation

[![](https://mermaid.ink/img/pako:eNp9VE1v2zAM_SuCLtuAJLAbO6l9CLClGBBgHYIW7WHwhbUZV4AteZIcrAvy30c5VmAvaXXRB_nIx0dJB56rAnnKDf5uUeZ4J6DUUGc6k4wG5FZp9mRQ-5MGtBW5aEBa9nW7uXb8rTVCojE_VCnyaw53YOEFDDqbt1dKNexJWlF1ZvYMlSi80Q1HYrpaUc6UPbYvtbBsW0GObK0RrFCSPbgajB2CyJswI0LpKTRYZCALttUqJ5MHn5IPQwzXUPUOP5W9ZOjGKNXU893IvXPusP8jHEXyc-Wl7J6gUCLL-MZ-MkxSmn3PtpiwpkJSjVn9xqAEITM-DIbyzKZf-u2Y1Grl9SchYY-9jBu5U7rulPS4K71xgFHRPtb0Uucu-HcQ1RjxPpsHdKV1sKFSg8L8_EHWtZI7oesuzHUBfFcoXavdtTGNkubsPGrIxRU7-bLPj23u7s0XPuGlFgVPrW5xwmskDd2WH1y0jNtXrDHjKS0L3EFbWeqaPBKMnsIvpWqP1KotX3m6g8rQrm1cz_vXeHYhJVCvVSstT-fRsovB0wP_w9PFcpbcBEEQxYvoNl6Q7Y0Ok1l8E8fBMo6SeRTOw-OE_-1yhrNgESaLJLoNw2WUhPGEYyHosd-f_oPuWzj-A-2mUPk?type=png)](https://mermaid.live/view#pako:eNp9VE1v2zAM_SuCLtuAJLAbO6l9CLClGBBgHYIW7WHwhbUZV4AteZIcrAvy30c5VmAvaXXRB_nIx0dJB56rAnnKDf5uUeZ4J6DUUGc6k4wG5FZp9mRQ-5MGtBW5aEBa9nW7uXb8rTVCojE_VCnyaw53YOEFDDqbt1dKNexJWlF1ZvYMlSi80Q1HYrpaUc6UPbYvtbBsW0GObK0RrFCSPbgajB2CyJswI0LpKTRYZCALttUqJ5MHn5IPQwzXUPUOP5W9ZOjGKNXU893IvXPusP8jHEXyc-Wl7J6gUCLL-MZ-MkxSmn3PtpiwpkJSjVn9xqAEITM-DIbyzKZf-u2Y1Grl9SchYY-9jBu5U7rulPS4K71xgFHRPtb0Uucu-HcQ1RjxPpsHdKV1sKFSg8L8_EHWtZI7oesuzHUBfFcoXavdtTGNkubsPGrIxRU7-bLPj23u7s0XPuGlFgVPrW5xwmskDd2WH1y0jNtXrDHjKS0L3EFbWeqaPBKMnsIvpWqP1KotX3m6g8rQrm1cz_vXeHYhJVCvVSstT-fRsovB0wP_w9PFcpbcBEEQxYvoNl6Q7Y0Ok1l8E8fBMo6SeRTOw-OE_-1yhrNgESaLJLoNw2WUhPGEYyHosd-f_oPuWzj-A-2mUPk)

### Description

> Explain the flow.

---

## Review Submission

[![](https://mermaid.ink/img/pako:eNp9VMFu2zAM_RWBl22AEyROUjs6BNhaDAiwDkWL9jD4otqMK8CWPEnO1gX591GOldlrNl4kio_kIynpALkuEDhY_N6iyvFGitKIOjOZYiQid9qwR4smnDTCOJnLRijHPt5tLx1_aq1UaO0XXcr8EuBGOPEsLHpbsFdaN-xROVl1ZvYkKlkEoxdPYrLZUE7OHtrnWjp2j3uJP2gh7tYNwYQi7IgIP4UUDplQBbszOidTcD4lHYYY7kXVA75q95aZl1GqSeC5VXsP7nz_9vAUCefL4uyWXEWJLIOte2eZojT7nm0RsaZC6hZz5pWJUkiVwTAYqjObfhvUManNJvSdGij2GNo3JHdhGh46KjdEmbztcBf2s5DV2OPfPO7RF9W5DWkMSgrrf7Jea7WTpu7CXC49zIPStUbRYhut7Bk8GkXfle6KWSv1Hzh7_9Dm_tJ8gAhKIwvgzrQYQY2mFl6Fgw-YgXvBGjPgtC1wJ9rK0cjUkdzo_n_Tug6eRrflC_CdqCxpbeMH3j_BM4SageZat8oBj-NVFwP4AX6SupzOF0k8T-brZJGmiwhegafLaZyuk1l8labpfDlbHSP41eWcTZMFAUmuVut4Gc_iCLCQ9MRvT79A9xkcfwNI6U1l?type=png)](https://mermaid.live/view#pako:eNp9VMFu2zAM_RWBl22AEyROUjs6BNhaDAiwDkWL9jD4otqMK8CWPEnO1gX591GOldlrNl4kio_kIynpALkuEDhY_N6iyvFGitKIOjOZYiQid9qwR4smnDTCOJnLRijHPt5tLx1_aq1UaO0XXcr8EuBGOPEsLHpbsFdaN-xROVl1ZvYkKlkEoxdPYrLZUE7OHtrnWjp2j3uJP2gh7tYNwYQi7IgIP4UUDplQBbszOidTcD4lHYYY7kXVA75q95aZl1GqSeC5VXsP7nz_9vAUCefL4uyWXEWJLIOte2eZojT7nm0RsaZC6hZz5pWJUkiVwTAYqjObfhvUManNJvSdGij2GNo3JHdhGh46KjdEmbztcBf2s5DV2OPfPO7RF9W5DWkMSgrrf7Jea7WTpu7CXC49zIPStUbRYhut7Bk8GkXfle6KWSv1Hzh7_9Dm_tJ8gAhKIwvgzrQYQY2mFl6Fgw-YgXvBGjPgtC1wJ9rK0cjUkdzo_n_Tug6eRrflC_CdqCxpbeMH3j_BM4SageZat8oBj-NVFwP4AX6SupzOF0k8T-brZJGmiwhegafLaZyuk1l8labpfDlbHSP41eWcTZMFAUmuVut4Gc_iCLCQ9MRvT79A9xkcfwNI6U1l)

### Description

> Explain the flow.

---

## Fetch Places

[![](https://mermaid.ink/img/pako:eNp9VFFv2yAQ_iuIl3WSE8VOqBseIm2LKkVqpqpS-zD5hdoXB4mAB7haFuW_73BCZq9ZecDgu--77-6AAy1NBZRTBz9b0CUspait2BW20ASHKL2x5NmBjX8aYb0sZSO0J18eV9d-f22d1ODcg6llec1hKbx4FQ6CLdqVMQ151l6qzkxehJJVNIYRRIwWC4zJyVNQ6zx5kDiZDXlUogRHbjZSebCOI1spvDQ6IY2VJSQEfDn-3KdDHmQbSOWnoMIDEbpCpEFSdwnWyepT9NdCnR2-G_9eexiDUKOYyUq_BecO-y8iSES_kDgna4SKGkhBV_6TIxrDvJ3VVpilAqwn8XZPRC2kLmifDPRFzXkZt0NRi0XsDCf3WLEtWQucpa7PFY6wK03r_GGQdSQbvS_0if1eSDWE_F_PE4TkPlTVSzN-P5CAhK3V8eiEk3S9KH_PXN-_369Bn5bSNWpP1PBk0oTWVlaUe9tCQndgdyJs6SFQFNRvYQcF5bisYCNa5bGD-ogwvDA_jNlFpDVtvaV8I5TDXduE_p_v7MUF6wD2m2m1p5ylHQXlB_qL8oyx8V02Y1nKpinLU5bQPeWz6TjN5rfzjOX5hGX57JjQ313MyTi_m2WTHM1TdstYOk8oVBLfhPXp2ehej-Mf-Mtdgw?type=png)](https://mermaid.live/view#pako:eNp9VFFv2yAQ_iuIl3WSE8VOqBseIm2LKkVqpqpS-zD5hdoXB4mAB7haFuW_73BCZq9ZecDgu--77-6AAy1NBZRTBz9b0CUspait2BW20ASHKL2x5NmBjX8aYb0sZSO0J18eV9d-f22d1ODcg6llec1hKbx4FQ6CLdqVMQ151l6qzkxehJJVNIYRRIwWC4zJyVNQ6zx5kDiZDXlUogRHbjZSebCOI1spvDQ6IY2VJSQEfDn-3KdDHmQbSOWnoMIDEbpCpEFSdwnWyepT9NdCnR2-G_9eexiDUKOYyUq_BecO-y8iSES_kDgna4SKGkhBV_6TIxrDvJ3VVpilAqwn8XZPRC2kLmifDPRFzXkZt0NRi0XsDCf3WLEtWQucpa7PFY6wK03r_GGQdSQbvS_0if1eSDWE_F_PE4TkPlTVSzN-P5CAhK3V8eiEk3S9KH_PXN-_369Bn5bSNWpP1PBk0oTWVlaUe9tCQndgdyJs6SFQFNRvYQcF5bisYCNa5bGD-ogwvDA_jNlFpDVtvaV8I5TDXduE_p_v7MUF6wD2m2m1p5ylHQXlB_qL8oyx8V02Y1nKpinLU5bQPeWz6TjN5rfzjOX5hGX57JjQ313MyTi_m2WTHM1TdstYOk8oVBLfhPXp2ehej-Mf-Mtdgw)

### Description

> Explain the flow.

---


# 5. Conclusion

> Summarize the overall architecture and explain how this document will support the implementation of the HBnB application.

