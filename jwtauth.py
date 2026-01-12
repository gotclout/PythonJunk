from jwt.algorithms import RSAAlgorithm


def validate_jwt_token(token, tenant_id, client_id) -> dict | None:
  """
  Validate the specified JWT token from Azure via pub key

  :param token: Is the str JWT token to validate
  :param tenant_id: Is the str Azure AD tenant id
  :param client_id: Is the Demand Assist client id.
  :return res: Decoded token if successfully validated, otherwise None
  """
  jwks = None

  try:
    # 1. Get public keys
    jwks_uri = f"https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys"
    jwks_res = requests.get(jwks_uri)

    jwks_res.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    jwks = jwks_response.json()

    # 2. Get the correct key
    header = jwt.get_unverified_header(token)
    kid    = header.get("kid")

    if not kid:
      self.logger.info("Error: 'kid' claim not found in token header")

    pk = None

    for key_data in jwks.get("keys", []):
      if key_data.get("kid") == kid:
        pk = RSAAlgorithm.from_jwk(key_data) # Missing this now
        break

    if not pk:
      print(f"Error: Public key with kid '{kid}' not found")

    # 3. Decode and verify the token
    jwks = jwt.decode(
      token,
      pk,
      algorithms=["RS256"],
      audience=client_id,
      issuer=f"https://sts.windows.net/{tenant_id}/",
    )

    return decoded_token

  except requests.exceptions.RequestException as e:
    logger.error("Error fetching JWKS: {e}")
  except jwt.exceptions.PyJWTError as e:
    print(f"Error decoding or verifying token: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

  return jwks
