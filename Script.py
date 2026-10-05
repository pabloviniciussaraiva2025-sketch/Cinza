-- Coloque este script em ServerScriptService no Roblox Studio
local Players = game:GetService("Players")
local InsertService = game:GetService("InsertService")

-- ID do pacote Korblox Deathspeaker
local KORBLOX_PACKAGE_ID = 139602840 

local function onCharacterAdded(character)
	-- Aguarda o personagem carregar completamente
	local humanoid = character:WaitForChild("Humanoid")
	local rootPart = character:WaitForChild("HumanoidRootPart")
	task.wait(0.1)
	
	-- 1. Mudar a cor do personagem para cinza (Medium stone grey)
	for _, part in ipairs(character:GetChildren()) do
		if part:IsA("BasePart") and part.Name ~= "HumanoidRootPart" then
			part.BrickColor = BrickColor.new("Medium stone grey")
		end
	end
	
	-- 2. Aplicar a Perna Direita da Korblox
	local success, model = pcall(function()
		return InsertService:LoadAsset(KORBLOX_PACKAGE_ID)
	end)
	
	if success and model then
		-- Procura pela perna direita no pacote Korblox
		local rightLeg = model:FindFirstChild("Right Leg", true) or model:FindFirstChild("RightLeg", true)
		
		if rightLeg then
			-- Remove a perna direita antiga do jogador
			local oldLeg = character:FindFirstChild("Right Leg") or character:FindFirstChild("RightLeg")
			if oldLeg then oldLeg:Destroy() end
			
			-- Clona e adiciona a nova perna Korblox
			local newLeg = rightLeg:Clone()
			newLeg.Parent = character
			
			-- Adapta para o tipo de corpo R6 ou R15
			if humanoid.RigType == Enum.HumanoidRigType.R15 then
				-- Para R15, o processo geralmente substitui os componentes (RightThigh, RightLowerLeg, RightFoot)
				-- Este script básico funciona melhor em R6. Se seu jogo for R15, use uma MeshPart específica.
				newLeg.BrickColor = BrickColor.new("Medium stone grey")
			else
				-- Configuração básica para R6
				newLeg.BrickColor = BrickColor.new("Medium stone grey")
			end
		end
		model:Destroy() -- Limpa o modelo temporário baixado
	else
		warn("Não foi possível carregar o pacote Korblox: ", model)
	end
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
